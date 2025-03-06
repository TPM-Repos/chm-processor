Remove(String) Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedFeatureParameterCollection Class](topic14225.md) > [Remove Method](topic14234.md) : Remove(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_address_
    The address of the additional feature parameter to remove.

Glossary Item Box

Removes the additional feature parameter with the specified name from the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Remove( _
       ByVal _address_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CapturedFeatureParameterCollection](topic14225.md)
    Dim address As String
    Dim value As Boolean
     
    value = instance.Remove(address)  
  
C#|   
---|---  
      
    
    public bool Remove( 
       string _address_
    )  
  
#### Parameters

 _address_
    The address of the additional feature parameter to remove.

#### Return Value

True if the additional feature parameter was found and removed, otherwise false.

# Remarks

This operation has O(N) running time.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CapturedFeatureParameterCollection Class](topic14225.md)   
[CapturedFeatureParameterCollection Members](topic14226.md)   
[Overload List](topic14234.md)


