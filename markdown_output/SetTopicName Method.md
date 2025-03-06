SetTopicName Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [HelpProvider Class](topic844.md) : SetTopicName Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_control_
    Control to set the topic name on.

_value_
    The help topic name to set on the control.

Glossary Item Box

Sets the help topic name for the specified control. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Sub SetTopicName( _
       ByVal _control_ As DependencyObject, _
       ByVal _value_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim control As DependencyObject
    Dim value As String
     
    [HelpProvider](topic844.md).SetTopicName(control, value)  
  
C#|   
---|---  
      
    
    public static void SetTopicName( 
       DependencyObject _control_ ,
       string _value_
    )  
  
#### Parameters

 _control_
    Control to set the topic name on.
_value_
    The help topic name to set on the control.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[HelpProvider Class](topic844.md)   
[HelpProvider Members](topic845.md)


