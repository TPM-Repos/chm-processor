Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PollingConnectorBase Class   
[Members](topic1915.md)   
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) : PollingConnectorBase Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides a base class for connectors which use a polling strategy. 

# Object Model

![](dotnetdiagramimages/image66.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustInherit Class PollingConnectorBase 
       Inherits [ConnectorBase](topic1834.md)
       Implements [IConnector](topic1697.md), [DriveWorks.Applications.Extensibility.IApplicationPlugin](topic2004.md), [DriveWorks.Extensibility.IExtension](topic7152.md)   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [PollingConnectorBase](topic1914.md)  
  
C#|   
---|---  
      
    
    public abstract class PollingConnectorBase : [ConnectorBase](topic1834.md), [IConnector](topic1697.md), [DriveWorks.Applications.Extensibility.IApplicationPlugin](topic2004.md), [DriveWorks.Extensibility.IExtension](topic7152.md)    
  
# Inheritance Hierarchy

System.Object  
[DriveWorks.Applications.Autopilot.Extensibility.ConnectorBase](topic1834.md)  
**DriveWorks.Applications.Autopilot.Extensibility.PollingConnectorBase**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[PollingConnectorBase Members](topic1915.md)   
[DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md)


