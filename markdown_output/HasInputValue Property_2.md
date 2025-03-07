Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
HasInputValue Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ControlBase Class](topic7698.md) : HasInputValue Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Returns true if the current control has an input value. A control's input value is the main property of the control, editable through the control's interface. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <EditorBrowsableAttribute(EditorBrowsableState.Advanced)>
    Public Overridable ReadOnly Property HasInputValue As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ControlBase](topic7698.md)
    Dim value As Boolean
     
    value = instance.HasInputValue  
  
C#|   
---|---  
      
    
    [EditorBrowsableAttribute(EditorBrowsableState.Advanced)]
    public virtual bool HasInputValue {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ControlBase Class](topic7698.md)   
[ControlBase Members](topic7699.md)


