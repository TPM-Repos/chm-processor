Remove(String) Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedInstanceCollection Class](topic14274.md) > [Remove Method](topic14282.md) : Remove(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_address_
    The address of the instance to remove.

Glossary Item Box

Removes the instance with the specified address from the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Remove( _
       ByVal _address_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CapturedInstanceCollection](topic14274.md)
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
    The address of the instance to remove.

#### Return Value

True if the instance was found and removed, otherwise false.

# Remarks

This operation has O(N) running time.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CapturedInstanceCollection Class](topic14274.md)   
[CapturedInstanceCollection Members](topic14275.md)   
[Overload List](topic14282.md)


