package com.company.base.conf;

import org.springframework.test.context.DynamicPropertyRegistry;
import com.company.base.PojaGenerated;

@PojaGenerated
public class BucketConf {

  void configureProperties(DynamicPropertyRegistry registry) {
    registry.add("aws.s3.bucket", () -> "dummy-bucket");
  }
}
