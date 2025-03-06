ToArray Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ITableValue Interface](topic2331.md) : ToArray Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Creates a two dimensional object array containing the values from the array value. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function ToArray() As Object(,)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ITableValue](topic2331.md)
    Dim value() As Object
     
    value = instance.ToArray()  
  
C#|   
---|---  
      
    
    object[,] ToArray()  
  
# Remarks

Wherever possible this method should be avoided as it can be very expensive in terms of memory and time taken.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ITableValue Interface](topic2331.md)   
[ITableValue Members](topic2332.md)


