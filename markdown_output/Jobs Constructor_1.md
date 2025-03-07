Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Jobs Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Jobs Class](topic3615.md) : Jobs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_inProgressJobs_
    The jobs currently being processed.

_pendingJobs_
    The jobs in the pool waiting to be processed.

Glossary Item Box

Creates an instance of the [Jobs](topic3615.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _inProgressJobs_() As [Job](topic3582.md), _
       ByVal _pendingJobs_() As [Job](topic3582.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim inProgressJobs() As [Job](topic3582.md)
    Dim pendingJobs() As [Job](topic3582.md)
     
    Dim instance As New [Jobs](topic3615.md)(inProgressJobs, pendingJobs)  
  
C#|   
---|---  
      
    
    public Jobs( 
       [Job](topic3582.md)[] _inProgressJobs_ ,
       [Job](topic3582.md)[] _pendingJobs_
    )  
  
#### Parameters

 _inProgressJobs_
    The jobs currently being processed.
_pendingJobs_
    The jobs in the pool waiting to be processed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Jobs Class](topic3615.md)   
[Jobs Members](topic3616.md)


