_T_
    

Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GroupPollingConnectorBase<T> Class   
[Members](topic1879.md)   
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) : GroupPollingConnectorBase<T> Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides a base class for group connectors which use a polling strategy. 

# Object Model

![](dotnetdiagramimages/image63.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustInherit Class GroupPollingConnectorBase(Of T As [GroupConnectorInformation](topic3084.md)) 
       Inherits [GroupConnectorBase(Of T)](topic1857.md)
       Implements [IGroupConnector](topic1706.md)   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupPollingConnectorBase(Of T)](topic1878.md)  
  
C#|   
---|---  
      
    
    public abstract class GroupPollingConnectorBase<T> : [GroupConnectorBase<T>](topic1857.md), [IGroupConnector](topic1706.md)  
    where T: [GroupConnectorInformation](topic3084.md)  
  
# Type Parameters

_T_
    

# Inheritance Hierarchy

System.Object  
[DriveWorks.Applications.Autopilot.Extensibility.GroupConnectorBase<T>](topic1857.md)  
**DriveWorks.Applications.Autopilot.Extensibility.GroupPollingConnectorBase <T>**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupPollingConnectorBase<T> Members](topic1879.md)   
[DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md)


