Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EventProxyReportWriter Constructor(IReportWriter)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) > [EventProxyReportWriter Class](topic10392.md) > [EventProxyReportWriter Constructor](topic10398.md) : EventProxyReportWriter Constructor(IReportWriter)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_writer_
    The writer to which to proxy reporting calls.

Glossary Item Box

Initializes a new instance of the [EventProxyReportWriter](topic10392.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _writer_ As [IReportWriter](topic10344.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim writer As [IReportWriter](topic10344.md)
     
    Dim instance As New [EventProxyReportWriter](topic10392.md)(writer)  
  
C#|   
---|---  
      
    
    public EventProxyReportWriter( 
       [IReportWriter](topic10344.md) _writer_
    )  
  
#### Parameters

 _writer_
    The writer to which to proxy reporting calls.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[EventProxyReportWriter Class](topic10392.md)   
[EventProxyReportWriter Members](topic10393.md)   
[Overload List](topic10398.md)


