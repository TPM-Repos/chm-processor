Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
JobTimeOut Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [JobRequestTagInformation Class](topic3604.md) : JobTimeOut Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the job timeout for the Agent. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property JobTimeOut As TimeSpan  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [JobRequestTagInformation](topic3604.md)
    Dim value As TimeSpan
     
    value = instance.JobTimeOut  
  
C#|   
---|---  
      
    
    public TimeSpan JobTimeOut {get;}  
  
# Remarks

If the Agent timeout is reached the componant will be marked as failed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[JobRequestTagInformation Class](topic3604.md)   
[JobRequestTagInformation Members](topic3605.md)


