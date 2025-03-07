Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Find Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedDimensionCollection Class](topic14162.md) : Find Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the dimension to look for.

_throwIfMissing_
    True to throw an exception if a property with the given name can't be found, otherwise, a null reference is returned.

Glossary Item Box

Looks for a dimension with the given name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Find( _
       ByVal _name_ As String, _
       ByVal _throwIfMissing_ As Boolean _
    ) As [CapturedDimension](topic14154.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CapturedDimensionCollection](topic14162.md)
    Dim name As String
    Dim throwIfMissing As Boolean
    Dim value As [CapturedDimension](topic14154.md)
     
    value = instance.Find(name, throwIfMissing)  
  
C#|   
---|---  
      
    
    public [CapturedDimension](topic14154.md) Find( 
       string _name_ ,
       bool _throwIfMissing_
    )  
  
#### Parameters

 _name_
    The name of the dimension to look for.
_throwIfMissing_
    True to throw an exception if a property with the given name can't be found, otherwise, a null reference is returned.

#### Return Value

A dimension for the specified name.

# Exceptions

Exception| Description  
---|---  
[DriveWorks.ItemNotFoundException](topic3571.md)| A dimension with the given name couldn't be found.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CapturedDimensionCollection Class](topic14162.md)   
[CapturedDimensionCollection Members](topic14163.md)


