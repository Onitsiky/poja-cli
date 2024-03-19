import poja.sed as sed


def set_sonar(dir, exclude):

    sonar_plugins = """id "org.sonarqube" version "4.4.1.3373" """
    sonar_conf = """sonarqube {
    properties {
    }
} """
    sonar_env = """env:
  SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }} """
    sonar_ci = """- name: Cache SonarCloud packages
        uses: actions/cache@v2
        with:
          path: ~/.sonar/cache
          key: sonar-${{ runner.os }}-${{ hashFiles('build.gradle') }}
          restore-keys: sonar-${{ runner.os }}-

      - name: Code quality and coverage analysis
        run: |
         ./gradlew sonarqube --info \\
         -Dsonar.host.url=https://sonarcloud.io \\
         -Dsonar.organization=${{ vars.SONAR_ORG }} \\
         -Dsonar.projectKey=${{ vars.SONAR_PJ_KEY }} \\
         -Dsonar.projectName=${{ vars.SONAR_PJ_NAME }} \\
         -Dsonar.coverage.jacoco.xmlReportPaths=build/reports/jacoco/test/jacocoTestReport.xml \\
         -Dsonar.java.checkstyle.reportPaths=build/reports/checkstyle/main.xml,build/reports/checkstyle/test.xml
 """

    sed.find_replace(dir, "<?sonar-java-plugins>", sonar_plugins, exclude)
    sed.find_replace(dir, "<?sonar-conf>", sonar_conf, exclude)
    sed.find_replace(dir, "<?sonar-env>", sonar_env, exclude)
    sed.find_replace(dir, "<?sonar-ci>", sonar_ci, exclude)
