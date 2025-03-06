ReportWriterBase Class Members   
See Also Properties Methods [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10476.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) : ReportWriterBase Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [ReportWriterBase](topic10476.md).

# Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [IsDisposed](topic10492.md)| Determines whether the report writer has been disposed.   
![Public Property](dotnetimages/publicProperty.gif)| [ProcessDepth](topic10493.md)| Gets the current depth of processes.   
Top

# Public Methods

| Name| Description  
---|---|---  
Public Method| [BeginProcess](topic10483.md)| Overloaded. Begins a process.   
Public Method| [EndProcess](topic10488.md)| Ends the current process.   
Public Method| [WriteEntry](topic10491.md)| Writes a report entry to the report.   
Top

# Protected Methods

| Name| Description  
---|---|---  
Protected Method| [AssertNotDisposed](topic10482.md)| Throws an System.ObjectDisposedException if the object has been disposed.   
Protected Method| [Dispose](topic10487.md)| Disposes the report writer and flushes its contents to the report.   
Protected Method| [Finalize](topic10489.md)| Handles object finalization.   
Protected Method| [Finish](topic10490.md)| Finishes the report, flushing any cached contents to the report if necessary.   
Top

# See Also

#### Reference

[ReportWriterBase Class](topic10476.md)   
[DriveWorks.Reporting Namespace](topic10334.md)


