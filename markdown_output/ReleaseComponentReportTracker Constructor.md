       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ReleaseComponentReportTracker Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReleaseComponentReportTracker Class](topic6292.md) : ReleaseComponentReportTracker Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_reportWriter_
    The report writer to use for the release component process.

Glossary Item Box

Create a new report tracker that reports release component information to the supplied report writer. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _reportWriter_ As [IReportWriter](topic10344.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim reportWriter As [IReportWriter](topic10344.md)
     
    Dim instance As New [ReleaseComponentReportTracker](topic6292.md)(reportWriter)  
  
C#|   
---|---  
      
    
    public ReleaseComponentReportTracker( 
       [IReportWriter](topic10344.md) _reportWriter_
    )  
  
#### Parameters

 _reportWriter_
    The report writer to use for the release component process.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleaseComponentReportTracker Class](topic6292.md)   
[ReleaseComponentReportTracker Members](topic6293.md)


