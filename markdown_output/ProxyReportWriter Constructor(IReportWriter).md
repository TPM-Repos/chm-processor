Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProxyReportWriter Constructor(IReportWriter)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Reporting Namespace](topic10334.md) > [ProxyReportWriter Class](topic10434.md) > [ProxyReportWriter Constructor](topic10440.md) : ProxyReportWriter Constructor(IReportWriter)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_writer_
    The writer to which to proxy reporting calls (may be null).

Glossary Item Box

Initializes a new instance of the [ProxyReportWriter](topic10434.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _writer_ As [IReportWriter](topic10344.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim writer As [IReportWriter](topic10344.md)
     
    Dim instance As New [ProxyReportWriter](topic10434.md)(writer)  
  
C#|   
---|---  
      
    
    public ProxyReportWriter( 
       [IReportWriter](topic10344.md) _writer_
    )  
  
#### Parameters

 _writer_
    The writer to which to proxy reporting calls (may be null).

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProxyReportWriter Class](topic10434.md)   
[ProxyReportWriter Members](topic10435.md)   
[Overload List](topic10440.md)


