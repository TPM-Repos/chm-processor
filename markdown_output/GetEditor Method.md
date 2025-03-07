Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetEditor Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IGroupConnector Interface](topic1706.md) : GetEditor Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets an editor that will providing editing features for the current connector. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetEditor() As [IGroupConnectorEditor](topic1716.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IGroupConnector](topic1706.md)
    Dim value As [IGroupConnectorEditor](topic1716.md)
     
    value = instance.GetEditor()  
  
C#|   
---|---  
      
    
    [IGroupConnectorEditor](topic1716.md) GetEditor()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IGroupConnector Interface](topic1706.md)   
[IGroupConnector Members](topic1707.md)


