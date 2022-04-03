package com.example.routingandfilteringgateway;

import com.netflix.discovery.EurekaClient;
import com.netflix.discovery.shared.Application;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.netflix.zuul.EnableZuulProxy;
import org.springframework.cloud.netflix.zuul.filters.ZuulProperties;
import org.springframework.context.annotation.Lazy;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;


@EnableZuulProxy
@SpringBootApplication
@EnableDiscoveryClient
@EnableAutoConfiguration
@RestController
public class RoutingAndFilteringGatewayApplication {

  @Autowired
  @Lazy
  private EurekaClient eurekaClient;

  @GetMapping("/hello")
  public String hello(){

    String hello="Hello world";
    for(Application a : eurekaClient.getApplications().getRegisteredApplications()){
      hello +=a.getName()+" \n"+ a.getInstances()+" ; \n";
    }
    return hello;
  }





  public static void main(String[] args) {
    SpringApplication.run(RoutingAndFilteringGatewayApplication.class, args);
  }

}
