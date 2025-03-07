Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Invoke(Point) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [MacroButton Class](topic8340.md) > [Invoke Method](topic8347.md) : Invoke(Point) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_clickPosition_
    

Glossary Item Box

Invokes the macro specified in the [MacroName](topic8351.md) property with the provided click position. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Invoke( _
       ByVal _clickPosition_ As Point _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [MacroButton](topic8340.md)
    Dim clickPosition As Point
    Dim value As Boolean
     
    value = instance.Invoke(clickPosition)  
  
C#|   
---|---  
      
    
    public bool Invoke( 
       Point _clickPosition_
    )  
  
#### Parameters

 _clickPosition_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[MacroButton Class](topic8340.md)   
[MacroButton Members](topic8341.md)   
[Overload List](topic8347.md)


