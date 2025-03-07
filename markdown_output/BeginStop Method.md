Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
BeginStop Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IAutopilotQueue Interface](topic1635.md) : BeginStop Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Stops the queue and returns a wait handle which can be used to wait for the queue to finish stopping. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function BeginStop() As WaitHandle  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IAutopilotQueue](topic1635.md)
    Dim value As WaitHandle
     
    value = instance.BeginStop()  
  
C#|   
---|---  
      
    
    WaitHandle BeginStop()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IAutopilotQueue Interface](topic1635.md)   
[IAutopilotQueue Members](topic1636.md)


