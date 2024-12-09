/**
 * @module 1-redis_op
 *
 * Defines the Redis connection and makes some operations
 */

import { promisify } from 'util'
import redis, {RedisClient, createClient} from 'redis'


/**
 * Create connection to the Redis server
 *
 * @param {string} host - The host or IP of host
 * @param {number} port - The port number on which server
 * is running
 *
 * @returns {RedisClient} - The Redis connection
 */
function createConnection(host, port) {
	const client = createClient(port, host)
	client.on('connect', () => {
		console.log('Redis client connected to the server')
	})

	client.on('error', err => {
		console.log(`Redis client not connected to the server: ${err}`)
	})
	return client
}

const client = createConnection('127.0.0.1', 6379)
const asyncSet = promisify(client.set).bind(client)
const asyncGet = promisify(client.get).bind(client)

/**
 * Sets new school
 * @param {string} schoolName - The key
 * @param {any} value - The value
 */
function setNewSchool(schoolName, value) {
	asyncSet(schoolName, value)
		.then(res => redis.print(null, res))
}

/**
 * Displays the school value
 * @param {string} schoolName - The school name
 */
function displaySchoolValue(schoolName) {
	asyncGet(schoolName)
		.then(res => console.log(res))
}


displaySchoolValue('ALX')
setNewSchool('ALXSanFrancisco', '100')
displaySchoolValue('ALXSanFrancisco')
