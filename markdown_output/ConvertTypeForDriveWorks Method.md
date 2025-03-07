Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ConvertTypeForDriveWorks Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [StoreConverter Class](topic9528.md) : ConvertTypeForDriveWorks Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    The value to convert.

Glossary Item Box

Converts the specified value to a DriveWorks safe value. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function ConvertTypeForDriveWorks( _
       ByVal _value_ As Object _
    ) As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim value As Object
    Dim value As Object
     
    value = [StoreConverter](topic9528.md).ConvertTypeForDriveWorks(value)  
  
C#|   
---|---  
      
    
    public static object ConvertTypeForDriveWorks( 
       object _value_
    )  
  
#### Parameters

 _value_
    The value to convert.

#### Return Value

The safe version of the value.

# Remarks

If value is already in a safe type then the original value is returned.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[StoreConverter Class](topic9528.md)   
[StoreConverter Members](topic9529.md)


