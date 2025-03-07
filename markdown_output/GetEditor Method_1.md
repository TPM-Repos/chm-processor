Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetEditor Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [GroupConnectorBase<T> Class](topic1857.md) : GetEditor Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the editor user interface for this group connector. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Function GetEditor() As [IGroupConnectorEditor](topic1716.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupConnectorBase(Of T)](topic1857.md)
    Dim value As [IGroupConnectorEditor](topic1716.md)
     
    value = instance.GetEditor()  
  
C#|   
---|---  
      
    
    public abstract [IGroupConnectorEditor](topic1716.md) GetEditor()  
  
#### Return Value

Either a System.Windows.Forms.Control or a System.Windows.UIElement.

# Remarks

This is responsible for all viewing and editing for the connector.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupConnectorBase<T> Class](topic1857.md)   
[GroupConnectorBase<T> Members](topic1858.md)


