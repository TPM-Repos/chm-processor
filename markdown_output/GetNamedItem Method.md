Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetNamedItem Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Project Class](topic3859.md) : GetNamedItem Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_qualifiedName_
    The fully qualified name of the item to get, e.g. "DWCalcTableOne.ColumnOne2".

Glossary Item Box

Attempts to find a matching named item in within DriveWorks, for example a calculation cell or variable. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <EditorBrowsableAttribute(EditorBrowsableState.Advanced)>
    Public Function GetNamedItem( _
       ByVal _qualifiedName_ As String _
    ) As [INamedItem](topic2249.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Project](topic3859.md)
    Dim qualifiedName As String
    Dim value As [INamedItem](topic2249.md)
     
    value = instance.GetNamedItem(qualifiedName)  
  
C#|   
---|---  
      
    
    [EditorBrowsableAttribute(EditorBrowsableState.Advanced)]
    public [INamedItem](topic2249.md) GetNamedItem( 
       string _qualifiedName_
    )  
  
#### Parameters

 _qualifiedName_
    The fully qualified name of the item to get, e.g. "DWCalcTableOne.ColumnOne2".

#### Return Value

The associated named item or null if nothing is found.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Project Class](topic3859.md)   
[Project Members](topic3860.md)


