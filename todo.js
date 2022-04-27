
function my_on_edit() {
  var sheet = SpreadsheetApp.getActiveSheet();

  var cell = sheet.getActiveCell();
  if (cell.getColumn() != 4) {
    return;
  }

  if (sheet.getName() == "todo") {
    if (cell.getValue().toLowerCase() == 'done') {
      var nextCell = cell.offset(0, 1);

      if (nextCell.getValue() === '') {
        var time = new Date();
        time = Utilities.formatDate(time, "GMT", "yyyy-MM-dd");
        nextCell.setValue(time);
      }

      moveRowFromTodoToDone(cell.getRow());
    }
  } 

  if (sheet.getName() == "done") {
    if (cell.getValue().toLowerCase() == 'todo') {
      var nextCell = cell.offset(0, 1);
      nextCell.setValue('');
      moveRowFromDoneToTodo(cell.getRow());
    }
  }
}

function moveRows(rowId, srcSheet, targetSheet) {
  var numColumns = srcSheet.getMaxColumns();

  var row = srcSheet.getRange(rowId, 1, 1, numColumns);

  targetSheet.insertRowAfter(1);
  var targetRow = targetSheet.getRange(2, 1, 1, numColumns);

  row.moveTo(targetRow);
  srcSheet.deleteRow(rowId);
}

function moveRowFromTodoToDone(rowId) {
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  var doneSheet = spreadsheet.getSheetByName("done");
  var todoSheet = spreadsheet.getSheetByName("todo");
  moveRows(rowId, todoSheet, doneSheet);
}

function moveRowFromDoneToTodo(rowId) {
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  var doneSheet = spreadsheet.getSheetByName("done");
  var todoSheet = spreadsheet.getSheetByName("todo");
  moveRows(rowId, doneSheet, todoSheet);
}