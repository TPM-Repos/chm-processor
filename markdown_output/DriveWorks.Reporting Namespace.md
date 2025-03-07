Collapse All Expand All  
---  
DriveWorks SDK Documentation  |   
---|---  
DriveWorks.Reporting Namespace   
See Also [Inheritance Hierarchy](topic10335.md) [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10334.md)  
[DriveWorks.Engine Assembly](topic2156.md) : DriveWorks.Reporting Namespace  
---  
  
Glossary Item Box

Provides types related to reporting capabilities. 

# Classes

| Class| Description  
---|---|---  
![Class](dotnetimages/Class.gif)| [CompositeReportWriter](topic10363.md) | Implements a report writer which writes to multiple other report writers.  
![Class](dotnetimages/Class.gif)| [EntryEventArgs](topic10379.md) | Provides data for events related to report entries.  
![Class](dotnetimages/Class.gif)| [EventProxyReportWriter](topic10392.md) | Implements a report writer which proxies to another report writer and raises events when processes and entries are written.  
![Class](dotnetimages/Class.gif)| [EventReportWriter](topic10409.md) | Implements a report writer which proxies to another report writer and raises events when processes and entries are written.  
![Class](dotnetimages/Class.gif)| [ProcessEventArgs](topic10424.md) | Provides data for events related to report processes.  
![Class](dotnetimages/Class.gif)| [ProxyReportWriter](topic10434.md) | Implements a report writer which proxies to another report writer.  
![Class](dotnetimages/Class.gif)| [ReportPackage](topic10451.md) | Implements a report writer where each top-level process is treated as a separate report, all of which are saved to a SQL Server CE database file.  
![Class](dotnetimages/Class.gif)| [ReportReader](topic10462.md) | Provides a reader for DriveWorks reports.  
![Class](dotnetimages/Class.gif)| [ReportWriterBase](topic10476.md) | Provides a simple base class from which report writers can inherit.  
![Class](dotnetimages/Class.gif)| [TraceReportWriter](topic10494.md) | Implements a report writer which writes to the tracing framework.  
  
# Interfaces

| Interface| Description  
---|---|---  
![Interface](dotnetimages/Interface.gif)| [IEventReportWriter](topic10336.md) | Represents a report writer that raises events.  
![Interface](dotnetimages/Interface.gif)| [IReportWriter](topic10344.md) | Provides a contract for report writers capable of logging reports for the DriveWorks Engine.  
![Interface](dotnetimages/Interface.gif)| [IReportWriterFactory](topic10355.md) | Provides a contract for an object which can create instances of implementations of the [IReportWriter](topic10344.md) interface for a set of related reports.  
  
# Delegates

| Delegate| Description  
---|---|---  
![Delegate](dotnetimages/Delegate.gif)| [EntryEventHandler](topic10508.md) | Represents a method that will handle events related to report entries.  
![Delegate](dotnetimages/Delegate.gif)| [ProcessEventHandler](topic10509.md) | Represents a method that will handle events related to report processes.  
  
# Enumerations

| Enumeration| Description  
---|---|---  
![Enumeration](dotnetimages/Enumeration.gif)| [ReportEntryType](topic10361.md) | Represents the type of an entry in a report.  
![Enumeration](dotnetimages/Enumeration.gif)| [ReportingLevel](topic10362.md) | Represents the reporting level.  
  
# See Also

#### Reference

[DriveWorks.Engine Assembly](topic2156.md)


