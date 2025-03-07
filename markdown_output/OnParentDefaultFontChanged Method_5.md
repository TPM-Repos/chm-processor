Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OnParentDefaultFontChanged Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ControlBase Class](topic7698.md) : OnParentDefaultFontChanged Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_newFont_
    

Glossary Item Box

Gives child controls a chance to update the font properties when the default font changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Sub OnParentDefaultFontChanged( _
       ByVal _newFont_ As [SimpleFont](topic8882.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ControlBase](topic7698.md)
    Dim newFont As [SimpleFont](topic8882.md)
     
    instance.OnParentDefaultFontChanged(newFont)  
  
C#|   
---|---  
      
    
    protected virtual void OnParentDefaultFontChanged( 
       [SimpleFont](topic8882.md) _newFont_
    )  
  
#### Parameters

 _newFont_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ControlBase Class](topic7698.md)   
[ControlBase Members](topic7699.md)


