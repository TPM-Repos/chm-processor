Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetRuleFromNamedItem Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Project Class](topic3859.md) : GetRuleFromNamedItem Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_qualifiedName_
    The fully qualified name of the item to get, e.g. "DWVariable1".

Glossary Item Box

Gets the rule for a named item within DriveWorks, for example a variable or constant. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <EditorBrowsableAttribute(EditorBrowsableState.Advanced)>
    Public Function GetRuleFromNamedItem( _
       ByVal _qualifiedName_ As String _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Project](topic3859.md)
    Dim qualifiedName As String
    Dim value As String
     
    value = instance.GetRuleFromNamedItem(qualifiedName)  
  
C#|   
---|---  
      
    
    [EditorBrowsableAttribute(EditorBrowsableState.Advanced)]
    public string GetRuleFromNamedItem( 
       string _qualifiedName_
    )  
  
#### Parameters

 _qualifiedName_
    The fully qualified name of the item to get, e.g. "DWVariable1".

#### Return Value

The rule associated with the named item.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Project Class](topic3859.md)   
[Project Members](topic3860.md)


