       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetFailed Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3603.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [JobQueue Class](topic3594.md) : SetFailed Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_jobId_
    The Id of the job that couldn't be processed.

Glossary Item Box

Flags the specified job as having failed to be processed by the current client. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub SetFailed( _
       ByVal _jobId_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [JobQueue](topic3594.md)
    Dim jobId As String
     
    instance.SetFailed(jobId)  
  
C#|   
---|---  
      
    
    public void SetFailed( 
       string _jobId_
    )  
  
#### Parameters

 _jobId_
    The Id of the job that couldn't be processed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[JobQueue Class](topic3594.md)   
[JobQueue Members](topic3595.md)

©2024 DriveWorks Ltd. All Rights Reserved.
