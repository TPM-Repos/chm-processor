Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Item Property   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ProjectComponentCollection Class](topic14462.md) : Item Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_index_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Default Property Item( _
       ByVal _index_ As Integer _
    ) As [ProjectSolidWorksComponent](topic14692.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectComponentCollection](topic14462.md)
    Dim index As Integer
    Dim value As [ProjectSolidWorksComponent](topic14692.md)
     
    value = instance.Item(index)  
  
C#|   
---|---  
      
    
    public [ProjectSolidWorksComponent](topic14692.md) this[ 
       int _index_
    ]; {get;}  
  
#### Parameters

 _index_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectComponentCollection Class](topic14462.md)   
[ProjectComponentCollection Members](topic14463.md)


