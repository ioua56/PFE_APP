package com.example.Monitoring;

import com.netflix.discovery.converters.Auto;
import de.codecentric.boot.admin.server.config.EnableAdminServer;
import de.codecentric.boot.admin.server.domain.entities.Application;
import de.codecentric.boot.admin.server.services.ApplicationRegistry;
import de.codecentric.boot.admin.server.services.InstanceRegistry;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.cloud.netflix.eureka.EnableEurekaClient;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Lazy;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

@Configuration
@EnableAutoConfiguration
@EnableAdminServer
@EnableEurekaClient
@RestController
public class MonitoringApplication {

	@Lazy
	@Autowired
	private ApplicationRegistry applicationRegistry;

	@GetMapping("/Services")
	public Flux<Application> hello(){
		return applicationRegistry.getApplications();
	}

	public static void main(String[] args) {
		SpringApplication.run(MonitoringApplication.class, args);
	}

}
