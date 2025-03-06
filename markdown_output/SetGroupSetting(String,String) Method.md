SetGroupSetting(String,String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Group Class](topic2958.md) > [SetGroupSetting Method](topic2980.md) : SetGroupSetting(String,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the setting.

_value_
    The value of the setting.

Glossary Item Box

Saves the named setting to the group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Sub SetGroupSetting( _
       ByVal _name_ As String, _
       ByVal _value_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Group](topic2958.md)
    Dim name As String
    Dim value As String
     
    instance.SetGroupSetting(name, value)  
  
C#|   
---|---  
      
    
    public void SetGroupSetting( 
       string _name_ ,
       string _value_
    )  
  
#### Parameters

 _name_
    The name of the setting.
_value_
    The value of the setting.

# Remarks

Using a null reference (Nothing in Visual Basic) as the value will delete the setting.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Group Class](topic2958.md)   
[Group Members](topic2959.md)   
[Overload List](topic2980.md)


