Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
InformationType Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IGroupConnectorRegistration Interface](topic1724.md) : InformationType Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the type of group connector data that this connector uses (must be derived from [DriveWorks.GroupConnectorInformation](topic3084.md)). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property InformationType As Type  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IGroupConnectorRegistration](topic1724.md)
    Dim value As Type
     
    value = instance.InformationType  
  
C#|   
---|---  
      
    
    Type InformationType {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IGroupConnectorRegistration Interface](topic1724.md)   
[IGroupConnectorRegistration Members](topic1725.md)


