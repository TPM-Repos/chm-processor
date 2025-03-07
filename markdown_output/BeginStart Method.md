Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
BeginStart Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IAutopilotQueue Interface](topic1635.md) : BeginStart Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Starts the queue on a new thread and returns a wait handle which can be used to wait for the queue to finish starting. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function BeginStart() As WaitHandle  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IAutopilotQueue](topic1635.md)
    Dim value As WaitHandle
     
    value = instance.BeginStart()  
  
C#|   
---|---  
      
    
    WaitHandle BeginStart()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IAutopilotQueue Interface](topic1635.md)   
[IAutopilotQueue Members](topic1636.md)


