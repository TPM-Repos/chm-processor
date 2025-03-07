Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateClickEventArgs(String,Point) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [FormControlValueChangeEventArgs Class](topic2895.md) > [CreateClickEventArgs Method](topic2901.md) : CreateClickEventArgs(String,Point) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_button_
    The name of the button that caused this event to occur.

_clickPosition_
    The System.Windows.Point of the click that caused the event to occur.

Glossary Item Box

Initializes an instance of [FormControlValueChangeEventArgs](topic2895.md) with values describing a click input. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function CreateClickEventArgs( _
       ByVal _button_ As String, _
       ByVal _clickPosition_ As Point _
    ) As [FormControlValueChangeEventArgs](topic2895.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim button As String
    Dim clickPosition As Point
    Dim value As [FormControlValueChangeEventArgs](topic2895.md)
     
    value = [FormControlValueChangeEventArgs](topic2895.md).CreateClickEventArgs(button, clickPosition)  
  
C#|   
---|---  
      
    
    public static [FormControlValueChangeEventArgs](topic2895.md) CreateClickEventArgs( 
       string _button_ ,
       Point _clickPosition_
    )  
  
#### Parameters

 _button_
    The name of the button that caused this event to occur.
_clickPosition_
    The System.Windows.Point of the click that caused the event to occur.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FormControlValueChangeEventArgs Class](topic2895.md)   
[FormControlValueChangeEventArgs Members](topic2896.md)   
[Overload List](topic2901.md)


