Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EventReportWriter Class   
[Members](topic10410.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) : EventReportWriter Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Implements a report writer which proxies to another report writer and raises events when processes and entries are written. 

# Object Model

![](dotnetdiagramimages/image523.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Class EventReportWriter 
       Inherits [ReportWriterBase](topic10476.md)
       Implements [IEventReportWriter](topic10336.md), [IReportWriter](topic10344.md)   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [EventReportWriter](topic10409.md)  
  
C#|   
---|---  
      
    
    public class EventReportWriter : [ReportWriterBase](topic10476.md), [IEventReportWriter](topic10336.md), [IReportWriter](topic10344.md)    
  
# Inheritance Hierarchy

System.Object  
[DriveWorks.Reporting.ReportWriterBase](topic10476.md)  
**DriveWorks.Reporting.EventReportWriter**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[EventReportWriter Members](topic10410.md)   
[DriveWorks.Reporting Namespace](topic10334.md)


