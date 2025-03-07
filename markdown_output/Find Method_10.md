Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Find Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ProjectFeatureCollection Class](topic14547.md) : Find Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the item to look for.

_throwIfMissing_
    True to throw an exception if an item with the given name can't be found, otherwise, a null reference is returned.

Glossary Item Box

Looks for a feature with the given name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Find( _
       ByVal _name_ As String, _
       ByVal _throwIfMissing_ As Boolean _
    ) As [ProjectFeature](topic14532.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectFeatureCollection](topic14547.md)
    Dim name As String
    Dim throwIfMissing As Boolean
    Dim value As [ProjectFeature](topic14532.md)
     
    value = instance.Find(name, throwIfMissing)  
  
C#|   
---|---  
      
    
    public [ProjectFeature](topic14532.md) Find( 
       string _name_ ,
       bool _throwIfMissing_
    )  
  
#### Parameters

 _name_
    The name of the item to look for.
_throwIfMissing_
    True to throw an exception if an item with the given name can't be found, otherwise, a null reference is returned.

#### Return Value

The item with the specified name.

# Exceptions

Exception| Description  
---|---  
[DriveWorks.ItemNotFoundException](topic3571.md)| An item with the given name couldn't be found.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectFeatureCollection Class](topic14547.md)   
[ProjectFeatureCollection Members](topic14548.md)


