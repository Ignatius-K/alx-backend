/**
 * @module 4-redis_advanced_op
 *
 * Explore some advanced operations in Redis
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
const asyncHset = promisify(client.hset).bind(client)
const asyncHgetAll = promisify(client.hgetall).bind(client)

/**
 * Sets new school
 * @param {string} schoolName - The key
 * @param {Object} value - The value
 */
function setNewSchool(schoolName, value) {
	asyncHset(schoolName, ...Object.entries(value).flat())
		.then(res => redis.print(null, res))
		.catch(err => redis.print(err, null))
}

/**
 * Displays the school value
 * @param {string} schoolName - The school name
 */
function displaySchoolValue(schoolName) {
	asyncHgetAll(schoolName)
		.then(res => redis.print(null, JSON.stringify(res)))
		.catch(err => redis.print(err, null))
}


displaySchoolValue('ALX')
setNewSchool('ALXSanFrancisco', {
	name: 'ALX',
	year: '2020'
})
displaySchoolValue('ALXSanFrancisco')
