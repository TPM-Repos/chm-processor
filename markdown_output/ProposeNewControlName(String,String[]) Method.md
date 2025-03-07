Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProposeNewControlName(String,String[]) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ControlCollection Class](topic7766.md) > [ProposeNewControlName Method](topic7780.md) : ProposeNewControlName(String,String[]) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_currentControlName_
    The current name of the control.

_reservedNames_
    An array of names which must not be used as the proposed control name.

Glossary Item Box

Proposes a new control name, for example in a copy and paste operation. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function ProposeNewControlName( _
       ByVal _currentControlName_ As String, _
       ByVal _reservedNames_() As String _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ControlCollection](topic7766.md)
    Dim currentControlName As String
    Dim reservedNames() As String
    Dim value As String
     
    value = instance.ProposeNewControlName(currentControlName, reservedNames)  
  
C#|   
---|---  
      
    
    public string ProposeNewControlName( 
       string _currentControlName_ ,
       string[] _reservedNames_
    )  
  
#### Parameters

 _currentControlName_
    The current name of the control.
_reservedNames_
    An array of names which must not be used as the proposed control name.

#### Return Value

A new control name, optionally suffixed with an index which makes the name unique.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ControlCollection Class](topic7766.md)   
[ControlCollection Members](topic7767.md)   
[Overload List](topic7780.md)


