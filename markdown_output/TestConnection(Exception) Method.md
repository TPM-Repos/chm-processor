TestConnection(Exception) Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IAutopilotService Interface](topic1654.md) > [TestConnection Method](topic1670.md) : TestConnection(Exception) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_exception_
    The exception that was thrown when attempting to connect to Pro Server.

Glossary Item Box

Tests the connection to the group currently in use by the [IAutopilotService](topic1654.md). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Function TestConnection( _
       ByRef _exception_ As Exception _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IAutopilotService](topic1654.md)
    Dim exception As Exception
    Dim value As Boolean
     
    value = instance.TestConnection(exception)  
  
C#|   
---|---  
      
    
    bool TestConnection( 
       ref Exception _exception_
    )  
  
#### Parameters

 _exception_
    The exception that was thrown when attempting to connect to Pro Server.

#### Return Value

True if the connection was successful, otherwise False.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IAutopilotService Interface](topic1654.md)   
[IAutopilotService Members](topic1655.md)   
[Overload List](topic1670.md)


