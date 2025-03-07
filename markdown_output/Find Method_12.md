Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Find Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ProjectInstanceCollection Class](topic14628.md) : Find Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_address_
    The address of the item to look for.

_throwIfMissing_
    True to throw an exception if an item with the given address can't be found, otherwise, a null reference is returned.

Glossary Item Box

Looks for an instance with the given address. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Find( _
       ByVal _address_ As String, _
       ByVal _throwIfMissing_ As Boolean _
    ) As [ProjectInstance](topic14616.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectInstanceCollection](topic14628.md)
    Dim address As String
    Dim throwIfMissing As Boolean
    Dim value As [ProjectInstance](topic14616.md)
     
    value = instance.Find(address, throwIfMissing)  
  
C#|   
---|---  
      
    
    public [ProjectInstance](topic14616.md) Find( 
       string _address_ ,
       bool _throwIfMissing_
    )  
  
#### Parameters

 _address_
    The address of the item to look for.
_throwIfMissing_
    True to throw an exception if an item with the given address can't be found, otherwise, a null reference is returned.

#### Return Value

The item with the specified address.

# Exceptions

Exception| Description  
---|---  
[DriveWorks.ItemNotFoundException](topic3571.md)| An item with the given address couldn't be found.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectInstanceCollection Class](topic14628.md)   
[ProjectInstanceCollection Members](topic14629.md)


