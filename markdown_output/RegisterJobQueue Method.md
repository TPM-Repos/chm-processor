Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RegisterJobQueue Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Group Class](topic2958.md) : RegisterJobQueue Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_jobType_
    The type of job that the queue will process.

Glossary Item Box

Registers a queue of jobs within DriveWorks that need to be processed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function RegisterJobQueue( _
       ByVal _jobType_ As String _
    ) As [JobQueue](topic3594.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Group](topic2958.md)
    Dim jobType As String
    Dim value As [JobQueue](topic3594.md)
     
    value = instance.RegisterJobQueue(jobType)  
  
C#|   
---|---  
      
    
    public [JobQueue](topic3594.md) RegisterJobQueue( 
       string _jobType_
    )  
  
#### Parameters

 _jobType_
    The type of job that the queue will process.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Group Class](topic2958.md)   
[Group Members](topic2959.md)


