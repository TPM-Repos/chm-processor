Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedSheetCollection Class](topic15017.md) : Add Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    

_scaleNumerator_
    

_scaleDenominator_
    

Glossary Item Box

Adds a new sheet. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Add( _
       ByVal _name_ As String, _
       ByVal _scaleNumerator_ As Double, _
       ByVal _scaleDenominator_ As Double _
    ) As [ReleasedSheet](topic15007.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedSheetCollection](topic15017.md)
    Dim name As String
    Dim scaleNumerator As Double
    Dim scaleDenominator As Double
    Dim value As [ReleasedSheet](topic15007.md)
     
    value = instance.Add(name, scaleNumerator, scaleDenominator)  
  
C#|   
---|---  
      
    
    public [ReleasedSheet](topic15007.md) Add( 
       string _name_ ,
       double _scaleNumerator_ ,
       double _scaleDenominator_
    )  
  
#### Parameters

 _name_
    
_scaleNumerator_
    
_scaleDenominator_
    

#### Return Value

The newly created sheet.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedSheetCollection Class](topic15017.md)   
[ReleasedSheetCollection Members](topic15018.md)


