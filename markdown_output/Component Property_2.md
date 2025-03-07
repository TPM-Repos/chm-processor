Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Component Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectComponentSet Class](topic4106.md) : Component Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the root component in the component set. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property Component As [ProjectComponent](topic6183.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectComponentSet](topic4106.md)
    Dim value As [ProjectComponent](topic6183.md)
     
    value = instance.Component  
  
C#|   
---|---  
      
    
    public [ProjectComponent](topic6183.md) Component {get;}  
  
# Remarks

If the component hasn't been loaded by a call to the [LoadComponent](topic4112.md) method, this property will return a null reference (Nothing in Visual Basic).

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectComponentSet Class](topic4106.md)   
[ProjectComponentSet Members](topic4107.md)


