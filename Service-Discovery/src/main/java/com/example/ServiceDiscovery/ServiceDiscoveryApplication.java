package com.example.ServiceDiscovery;

import com.netflix.discovery.DiscoveryClient;
import com.netflix.discovery.EurekaClient;
import com.netflix.discovery.shared.Application;
import com.netflix.discovery.shared.Applications;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.server.EnableEurekaServer;
import org.springframework.context.annotation.Lazy;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@EnableEurekaServer
@EnableAutoConfiguration
@RestController
public class ServiceDiscoveryApplication {

	@Autowired
	@Lazy
	private EurekaClient eurekaClient;

	@GetMapping("/Services")
	public String getPathologiesList(){

		String hello="Hello world";
		for(Application a : eurekaClient.getApplications().getRegisteredApplications()){
			hello +=a.getName()+" \n"+ a.getInstances()+" ; \n";
		}
		return hello;
	}

	public static void main(String[] args) {
		SpringApplication.run(ServiceDiscoveryApplication.class, args);
	}

}
