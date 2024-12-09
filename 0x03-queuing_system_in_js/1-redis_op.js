/**
 * @module 1-redis_op
 *
 * Defines the Redis connection and makes some operations
 */

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

/**
 * Sets new school
 * @param {string} schoolName - The key
 * @param {any} value - The value
 */
function setNewSchool(schoolName, value) {
	client.set(schoolName, value, (err, res) => redis.print(err, res))
}

/**
 * Displays the school value
 * @param {string} schoolName - The school name
 * @returns {string} - The value of the school
 */
function displaySchoolValue(schoolName) {
	client.get(schoolName, (_, res) => console.log(res))
}


displaySchoolValue('ALX')
setNewSchool('ALXSanFrancisco', '100')
displaySchoolValue('ALXSanFrancisco')
