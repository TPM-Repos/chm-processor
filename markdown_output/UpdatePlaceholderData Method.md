UpdatePlaceholderData Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [RollupDataTable Class](topic5240.md) : UpdatePlaceholderData Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_newData_
    The new placeholder data. If Nothing or an empty 2D array is passed in then this will clear the data.

Glossary Item Box

Updates the placeholder data with the new values. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub UpdatePlaceholderData( _
       ByVal _newData_(,) As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RollupDataTable](topic5240.md)
    Dim newData() As String
     
    instance.UpdatePlaceholderData(newData)  
  
C#|   
---|---  
      
    
    public void UpdatePlaceholderData( 
       string[,] _newData_
    )  
  
#### Parameters

 _newData_
    The new placeholder data. If Nothing or an empty 2D array is passed in then this will clear the data.

# Remarks

If the number of columns in the new data doesn't match the number of columns set for this table then an System.ArgumentException will be thrown.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RollupDataTable Class](topic5240.md)   
[RollupDataTable Members](topic5241.md)


