Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateClickEventArgs(String,String,String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [FormControlValueChangeEventArgs Class](topic2895.md) > [CreateClickEventArgs Method](topic2901.md) : CreateClickEventArgs(String,String,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_button_
    The name of the button that caused this event to occur.

_clickPositionX_
    The x co-ordinate of the click that caused the event to occur.

_clickPositionY_
    The y co-ordinate of the click that caused the event to occur.

Glossary Item Box

Initializes an instance of [FormControlValueChangeEventArgs](topic2895.md) with values describing a click input. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function CreateClickEventArgs( _
       ByVal _button_ As String, _
       ByVal _clickPositionX_ As String, _
       ByVal _clickPositionY_ As String _
    ) As [FormControlValueChangeEventArgs](topic2895.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim button As String
    Dim clickPositionX As String
    Dim clickPositionY As String
    Dim value As [FormControlValueChangeEventArgs](topic2895.md)
     
    value = [FormControlValueChangeEventArgs](topic2895.md).CreateClickEventArgs(button, clickPositionX, clickPositionY)  
  
C#|   
---|---  
      
    
    public static [FormControlValueChangeEventArgs](topic2895.md) CreateClickEventArgs( 
       string _button_ ,
       string _clickPositionX_ ,
       string _clickPositionY_
    )  
  
#### Parameters

 _button_
    The name of the button that caused this event to occur.
_clickPositionX_
    The x co-ordinate of the click that caused the event to occur.
_clickPositionY_
    The y co-ordinate of the click that caused the event to occur.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FormControlValueChangeEventArgs Class](topic2895.md)   
[FormControlValueChangeEventArgs Members](topic2896.md)   
[Overload List](topic2901.md)


