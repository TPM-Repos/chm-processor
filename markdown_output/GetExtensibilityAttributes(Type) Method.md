Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetExtensibilityAttributes(Type) Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Extensibility Namespace](topic1995.md) > [ILibraryInfo Interface](topic2055.md) > [GetExtensibilityAttributes Method](topic2060.md) : GetExtensibilityAttributes(Type) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_attributeType_
    The type of extensibility attribute to get.

Glossary Item Box

Gets the extensibility attributes of the specified type for the library. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Function GetExtensibilityAttributes( _
       ByVal _attributeType_ As Type _
    ) As Array  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ILibraryInfo](topic2055.md)
    Dim attributeType As Type
    Dim value As Array
     
    value = instance.GetExtensibilityAttributes(attributeType)  
  
C#|   
---|---  
      
    
    Array GetExtensibilityAttributes( 
       Type _attributeType_
    )  
  
#### Parameters

 _attributeType_
    The type of extensibility attribute to get.

#### Return Value

An array of the extensibility attribute of the specified type.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ILibraryInfo Interface](topic2055.md)   
[ILibraryInfo Members](topic2056.md)   
[Overload List](topic2060.md)


