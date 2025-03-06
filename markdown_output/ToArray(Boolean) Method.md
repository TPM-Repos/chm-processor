ToArray(Boolean) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Teams Class](topic11737.md) > [ToArray Method](topic11748.md) : ToArray(Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_includePermissions_
    True to include !, ?, * in the returned array if the associated permissions are set, false to return only team information.

Glossary Item Box

Copies all of the team identifiers to a new array and returns them. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function ToArray( _
       ByVal _includePermissions_ As Boolean _
    ) As String()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Teams](topic11737.md)
    Dim includePermissions As Boolean
    Dim value() As String
     
    value = instance.ToArray(includePermissions)  
  
C#|   
---|---  
      
    
    public string[] ToArray( 
       bool _includePermissions_
    )  
  
#### Parameters

 _includePermissions_
    True to include !, ?, * in the returned array if the associated permissions are set, false to return only team information.

#### Return Value

An array of team identifiers represented as strings.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Teams Class](topic11737.md)   
[Teams Members](topic11738.md)   
[Overload List](topic11748.md)


