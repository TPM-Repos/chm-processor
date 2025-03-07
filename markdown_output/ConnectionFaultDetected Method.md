Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ConnectionFaultDetected Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IAutopilotQueueManager Interface](topic1643.md) : ConnectionFaultDetected Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_exception_
    The exception that was thrown.

Glossary Item Box

Displays a retry connection dialog if one doesn't exist, and re-raises the [ConnectionFault](topic1653.md) event if required. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub ConnectionFaultDetected( _
       ByVal _exception_ As Exception _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IAutopilotQueueManager](topic1643.md)
    Dim exception As Exception
     
    instance.ConnectionFaultDetected(exception)  
  
C#|   
---|---  
      
    
    void ConnectionFaultDetected( 
       Exception _exception_
    )  
  
#### Parameters

 _exception_
    The exception that was thrown.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IAutopilotQueueManager Interface](topic1643.md)   
[IAutopilotQueueManager Members](topic1644.md)


