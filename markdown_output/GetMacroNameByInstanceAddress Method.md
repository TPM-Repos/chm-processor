Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetMacroNameByInstanceAddress Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [IPreviewDocument Interface](topic2263.md) : GetMacroNameByInstanceAddress Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_address_
    Address of the instance you want to find the macro for.

Glossary Item Box

Takes an instance address and returns the result of its click macro rule. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetMacroNameByInstanceAddress( _
       ByVal _address_ As String _
    ) As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IPreviewDocument](topic2263.md)
    Dim address As String
    Dim value As String
     
    value = instance.GetMacroNameByInstanceAddress(address)  
  
C#|   
---|---  
      
    
    string GetMacroNameByInstanceAddress( 
       string _address_
    )  
  
#### Parameters

 _address_
    Address of the instance you want to find the macro for.

#### Return Value

The name of the macro for the instance with the given address.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IPreviewDocument Interface](topic2263.md)   
[IPreviewDocument Members](topic2264.md)


