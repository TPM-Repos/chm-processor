Stopped Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IConnector Interface](topic1697.md) : Stopped Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Occurs when a connector has stopped. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event Stopped As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IConnector](topic1697.md)
    Dim handler As EventHandler
     
    AddHandler instance.Stopped, handler  
  
C#|   
---|---  
      
    
    event EventHandler Stopped  
  
# Remarks

Implementors should raise this event when the connector is stopped by the [Stop](topic1703.md) method, or when the connector is stopped internally for any reason.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IConnector Interface](topic1697.md)   
[IConnector Members](topic1698.md)


