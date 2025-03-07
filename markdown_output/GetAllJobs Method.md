Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetAllJobs Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Group Class](topic2958.md) : GetAllJobs Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_jobType_
    The type of jobs to retrieve.

Glossary Item Box

Gets all pending and currently in progress jobs that the current user has access to, for the specified job type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetAllJobs( _
       ByVal _jobType_ As String _
    ) As [Jobs](topic3615.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Group](topic2958.md)
    Dim jobType As String
    Dim value As [Jobs](topic3615.md)
     
    value = instance.GetAllJobs(jobType)  
  
C#|   
---|---  
      
    
    public [Jobs](topic3615.md) GetAllJobs( 
       string _jobType_
    )  
  
#### Parameters

 _jobType_
    The type of jobs to retrieve.

#### Return Value

All pending and currently in progress jobs for the specified job type.

# Remarks

This will take into account the connected user.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Group Class](topic2958.md)   
[Group Members](topic2959.md)


