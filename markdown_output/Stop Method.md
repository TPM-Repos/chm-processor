Stop Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IConnector Interface](topic1697.md) : Stop Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Stops the connector to prevent new specifications being received. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub Stop()   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IConnector](topic1697.md)
     
    instance.Stop()  
  
C#|   
---|---  
      
    
    void Stop()  
  
# Remarks

Any resources, for example, database connections, network sockets, and so on, should be closed by implementors of this method.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IConnector Interface](topic1697.md)   
[IConnector Members](topic1698.md)


