/**
 * @module 0-redis_client
 *
 * Defines the Redis connection
 */

import {RedisClient, createClient} from 'redis'


/**
 * Builds connection to the Redis server
 *
 * @param {string} host - The host or IP of host
 * @param {number} port - The port number on which server
 * is running
 *
 * @returns {Promise<RedisClient>} - The Redis connection
 */
function createConnection(host, port) {
	return new Promise((resolve, reject) => {
		const client = createClient(port, host)
		client.on('connect', () => {
			console.log('Redis client connected to the server')
			resolve(client)
		})

		client.on('error', err => {
			console.log(`Redis client not connected to the server: ${err}`)
			reject(err)
		})
	})
}

/**
 * main
 */
async function main() {
	try {
		await createConnection("127.0.0.1", 6379)
	} catch {
		process.exit()
	}
}

main()

